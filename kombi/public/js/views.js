(function($, Backbone, _, app) {
    var TemplateView = Backbone.View.extend({
        templateName: '',
        initialize: function() {
            this.template = _.template($(this.templateName).html());
        },
        render: function() {
            var context = this.getContext(),
                html = this.template(context);
            this.$el.html(html);
        },
        getContext: function() {
            return {};
        }
    });
    var IndexView = TemplateView.extend({
        templateName: "#deliveries-list",
        initialize: function(options) {
            var self = this;
            TemplateView.prototype.initialize.apply(this,arguments);
            app.collections.ready.done(function(){
                app.deliveries.fetch();
            });
        },
        getContext: function() {
            return {
                deliveries: app.deliveries || null,
                value: "ABC"
            };
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
