(function($, Backbone, _, app) {
    //app.collections.ready = $.getJSON(app.apiRoot);
    app.models.Delivery = Backbone.Model.extend({});
    /*app.collections.ready.done(function(data){*/
    app.collections.Deliveries = Backbone.Collection.extend({
        model: app.models.Delivery,
        url: app.apiRoot
    });
    app.deliveries = new app.collections.Deliveries();
    // });
})(jQuery, Backbone, _, app);
