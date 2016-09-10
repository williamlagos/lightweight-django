(function($, Backbone, _, app) {
    app.collections.ready = $.getJSON(app.apiRoot);
    app.collections.ready.done(function(data){
        app.models.Delivery = Backbone.Model.extend({
            get: function(attr){
                return this.attributes.objects[0][attr];
            }
        });    /*app.collections.ready = $.getJSON(app.apiRoot);
        app.collections.ready.done(function(data){*/
        app.collections.Deliveries = Backbone.Collection.extend({
            model: app.models.Delivery,
            url: data.deliveries
        });
        app.deliveries = new app.collections.Deliveries();
    });
    // });
})(jQuery, Backbone, _, app);
