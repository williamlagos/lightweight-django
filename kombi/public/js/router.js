(function($, Backbone, _, app) {
    var AppRouter = Backbone.Router.extend({
        routes: {
            '': 'home',
            'add': 'freight',
            'list': 'deliveries',
            'select': 'select',
            'help': 'help'
        },
        initialize: function(options) {
            this.current = null;
            Backbone.history.start();
        },
        home: function() {
            var view = new app.views.KombiView();
            this.render(view);
        },
        freight: function() {
            var view = new app.views.FreightView();
            $('#wrapper').toggleClass('toggled');
            this.render(view);
        },
        deliveries: function() {
            var view = new app.views.IndexView();
            $('#wrapper').toggleClass('toggled');
            this.render(view);
        },
        select: function() {
            var view = new app.views.SelectView();
            $('#wrapper').toggleClass('toggled');
            this.render(view);
        },
        help: function() {
            var view = new app.views.HelpView();
            $('#wrapper').toggleClass('toggled');
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
