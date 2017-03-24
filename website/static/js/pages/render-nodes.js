'use strict';

var $osf = require('js/osfHelpers');
var $ = require('jquery');
var m = require('mithril');
var LogFeed = require('js/components/logFeed.js');

// model for components, due to simplicity did not create a new file
var ComponentControl = {};

// binds to component scope in render_nodes.mako
$('.render-nodes-list').each(function() {
    $osf.applyBindings(ComponentControl, this);
});
