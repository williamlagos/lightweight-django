(function($, Backbone, _, app) {
    var Session = Backbone.Model.extend({
        defaults: {
            token: null
        },
        initialize: function(options){
            this.options = options;
            this.load();
        },
        load: function(){
            var token = localStorage.apiToken;
            if(token){
                this.set('token',token);
            }
        },
        save: function(token){
            this.set('token',token);
            if(token === null){
                localStorage.removeItem('apiToken');
            } else {
                localStorage.apiToken = token;
            }
        },
        delete: function(){
            this.save(null);
        },
        authenticated: function(){
            return this.get('token') !== null;
        },
    });
    app.session = new Session();
    app.models.Delivery = Backbone.Model.extend({});
    app.collections.Deliveries = Backbone.Collection.extend({
        model: app.models.Delivery,
        url: app.apiRoot
    });
    app.deliveries = new app.collections.Deliveries();
    // });
})(jQuery, Backbone, _, app);
