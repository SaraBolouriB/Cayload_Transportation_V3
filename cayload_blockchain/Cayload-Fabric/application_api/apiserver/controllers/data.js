const { Gateway, Wallets } = require('fabric-network');
const path = require('path');
const fs = require('fs');
const FabricCAServices = require('fabric-ca-client');



exports.register = async (req, res) => {
    try {
        username = req.body.username;
        await registerUser(username);
        res.status(200).json({response: "Done"});
    } catch (error) {
        console.error(`Failed to register: ${error}`);
        res.status(500).json({error: error});
    }
};

exports.query = async (req, res) => {
    try {
        username = req.body.username;
        const {contract, gateway} = await configNetwork(username);
        const result = await contract.evaluateTransaction('queryAllContracts');
        res.status(200).json({response: result.toString() });

        // Disconnect from the gateway.
        await gateway.disconnect();
        
    } catch (error) {
        console.error(`Failed to query: ${error}`);
        res.status(500).json({error: error});
    }
};

exports.queryContract = async (req, res) => {
    try{
        console.log('queryContract');
        username = req.body.username;
        const contractNumber = req.params.contractNumber;
        const {contract, gateway} = await configNetwork(username);
        const result = await contract.evaluateTransaction('queryContract', contractNumber);
        res.status(200).json({response: result.toString() });

        // Disconnect from the gateway.
        await gateway.disconnect();
    }
    catch (error) {
        console.error(`Failed to query contract: ${error}`);
        res.status(500).json({error: error});
    }

};

exports.addContract = async (req, res) => {
    try{
        console.log('add');
        const key = 'CONTRACT' + req.body.key;
        const data = req.body.data;
        const username = req.body.username;
        const {contract, gateway} = await configNetwork(username);
        await contract.submitTransaction('addContract', key, data, username);
        res.status(200).json({response: "Contract added"});
    
        // Disconnect from the gateway.
        await gateway.disconnect();
    }
    catch (error) {
        console.error(`Failed to add transaction: ${error}`);
        res.status(500).json({error: error});
    }


};

async function configNetwork(username) {
    // load the network configuration
    const ccpPath = path.resolve(__dirname, '..', '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
    const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

    // Create a new file system based wallet for managing identities.
    const walletPath = path.join(process.cwd(), 'wallet');
    const wallet = await Wallets.newFileSystemWallet(walletPath);
    console.log(`Wallet path: ${walletPath}`);

    // Check to see if we've already enrolled the user.
    const identity = await wallet.get(username);
    if (!identity) {
        console.log('An identity for the user ' + username + ' does not exist in the wallet');
        console.log('Run the registerUser.js application before retrying');
        return;
    }

    // Create a new gateway for connecting to our peer node.
    const gateway = new Gateway();
    await gateway.connect(ccp, { wallet, identity: username, discovery: { enabled: true, asLocalhost: true } });

    // Get the network (channel) our contract is deployed to.
    const network = await gateway.getNetwork('mychannel');

    // Get the contract from the network.
    const contract = network.getContract('cayload');

    return {contract, gateway};
};

async function registerUser(username) {
    try {
        // load the network configuration
        const ccpPath = path.resolve(__dirname, '..', '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
        const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new CA client for interacting with the CA.
        const caURL = ccp.certificateAuthorities['ca.org1.example.com'].url;
        const ca = new FabricCAServices(caURL);

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the user.
        const userIdentity = await wallet.get(username);
        if (userIdentity) {
            console.log('An identity for the user already exists in the wallet');
            return;
        }

        // Check to see if we've already enrolled the admin user.
        const adminIdentity = await wallet.get('admin');
        if (!adminIdentity) {
            console.log('An identity for the admin user "admin" does not exist in the wallet');
            console.log('Run the enrollAdmin.js application before retrying');
            return;
        }

        // build a user object for authenticating with the CA
        const provider = wallet.getProviderRegistry().getProvider(adminIdentity.type);
        const adminUser = await provider.getUserContext(adminIdentity, 'admin');

        // Register the user, enroll the user, and import the new identity into the wallet.
        const secret = await ca.register({
            affiliation: 'org1.department1',
            enrollmentID: username,
            role: 'client'
        }, adminUser);
        const enrollment = await ca.enroll({
            enrollmentID: username,
            enrollmentSecret: secret
        });
        const x509Identity = {
            credentials: {
                certificate: enrollment.certificate,
                privateKey: enrollment.key.toBytes(),
            },
            mspId: 'Org1MSP',
            type: 'X.509',
        };
        await wallet.put(username, x509Identity);
        console.log('Successfully registered and enrolled admin user ' + username +  ' and imported it into the wallet');

    } catch (error) {
        console.error(`Failed to register user: ${error}`);
        process.exit(1);
    }
};