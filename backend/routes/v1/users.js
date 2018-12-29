var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/:id', function(req, res, next) {
    var user_id = req.params['id'];
    res.status(200).end(JSON.stringify({'id':user_id, 'name':user_id + "_name"}));
});

module.exports = router;
