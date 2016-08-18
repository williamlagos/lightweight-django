(function($, Backbone, _, app) {
    var AppRouter = Backbone.Router.extend({
        routes: {
            '': 'home'
        },
        initialize: function(options) {
            this.contentElement = '#kombi';
            this.current = null;
            Backbone.history.start();
        },
        home: function() {
            var view = new app.views.IndexView({el: this.contentElement});
            this.render(view);
        },
        render: function(view) {
            if(this.current){
                this.current.$el = $();
                this.current.remove();
            }
            this.current = view;
            this.current.render();
        },
    });
    app.router = AppRouter;
})(jQuery, Backbone, _, app);
