var express = require('express');
var router = express.Router();

/* GET prediction listing. */
router.get('/:id', function(req, res, next) {
    var prediction_id = req.params['id'];
    res.status(200).end(JSON.stringify({'id':prediction_id, 'name':prediction_id + "_name"}));
});

module.exports = router;
