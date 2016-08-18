(function($, Backbone, _, app) {
    var IndexView = Backbone.View.extend({
        initialize: function() {
            this.template = _.template($('#kombi').html());
        },
        render: function() {
            var context = this.getContext(),
                html = this.template(context);
            this.$el.html(html);
        },
        getContext: function() {
            return {};
        },
    });
    var NavbarView = Backbone.View.extend({
        el: $('.navbar'),
        events: {
            'click #freight':'alert',
            'click #provider':'console'
        },
        alert: function() {
            alert('Hi!');
        },
        console: function() {
            alert('Ha!');
        }
    });
    app.views.NavbarView = NavbarView;
    app.views.IndexView = IndexView;
})(jQuery, Backbone, _, app);
