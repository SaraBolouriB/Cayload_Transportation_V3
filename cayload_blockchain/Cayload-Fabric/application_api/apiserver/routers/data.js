const express = require('express');
const dataControllers = require('../controllers/data');

const router = express.Router();

// router.get('/getAlldata/:channelName', dataControllers.getAllData);
router.get('/query', dataControllers.query);
router.get('/query/:contractNumber', dataControllers.queryContract);

router.post('/add', dataControllers.addContract);

router.post('/register', dataControllers.register)


module.exports = router;