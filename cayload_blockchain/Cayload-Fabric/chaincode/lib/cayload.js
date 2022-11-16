'use strict';

const { Contract } = require('fabric-contract-api');

class Cayload extends Contract {

    async initLedger(ctx) {
        console.info('============= START : Initialize Ledger ===========');
        const contracts = [
            {
                data: 'This is the first transaction, which must be original',
                signature: {
                    data_signed : 'This is the first transaction, which must be sigend by user',
                    username: 'Server',
                    public_key: 'No public key for this user'
                }
            },
        ];

        for (let i = 0; i < contracts.length; i++) {
            contracts[i].docType = 'contract';
            await ctx.stub.putState('CONTRACT' + i, Buffer.from(JSON.stringify(contracts[i])));
            console.info('Added <--> ', contracts[i]);
        }
        console.info('============= END : Initialize Ledger ===========');
    }

    async queryContract(ctx, contractNumber) {
        const contractAsBytes = await ctx.stub.getState(contractNumber); // get the contract from chaincode state
        if (!contractAsBytes || contractAsBytes.length === 0) {
            throw new Error(`${contractNumber} does not exist`);
        }
        console.log(contractAsBytes.toString());
        return contractAsBytes.toString();
    }

    async addContract(ctx, contractNumber, data, username) {
        console.info('============= START : Create contract ===========');
        const contract = {
            data: data,
            docType: 'contract',
            username: username
        };
        await ctx.stub.putState(contractNumber, Buffer.from(JSON.stringify(contract)));
        console.info('============= END : Create contract ===========');
    }

    async queryAllContracts(ctx) {
        const startKey = '';
        const endKey = '';
        const allResults = [];
        for await (const {key, value} of ctx.stub.getStateByRange(startKey, endKey)) {
            const strValue = Buffer.from(value).toString('utf8');
            let record;
            try {
                record = JSON.parse(strValue);
            } catch (err) {
                console.log(err);
                record = strValue;
            }
            allResults.push({ Key: key, Record: record });
        }
        console.info(allResults);
        return JSON.stringify(allResults);
    }

}

module.exports = Cayload;
