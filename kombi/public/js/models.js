(function($, Backbone, _, app) {
    var Deliveries = Backbone.Collection.extend({
        url:'/books'
    });
    app.collections = Deliveries;
})(jQuery, Backbone, _, app);
