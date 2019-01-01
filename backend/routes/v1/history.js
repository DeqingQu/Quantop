var express = require('express');
var router = express.Router();

/* GET history listing. */
router.get('/:id', function(req, res, next) {
    var history_id = req.params['id'];
    res.status(200).end(JSON.stringify({'id':history_id, 'name':history_id + "_name"}));
});

module.exports = router;
