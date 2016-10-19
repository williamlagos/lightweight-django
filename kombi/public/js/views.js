(function($, Backbone, _, app) {
    var TemplateView = Backbone.View.extend({
        templateName: '',
        el: '#content-wrapper',
        initialize: function() {
            this.template = _.template($(this.templateName).html());
        },
        render: function() {
            var context = this.getContext();
            var html = this.template(context);
            this.$el.html(html);
        },
        getContext: function() {
            return {};
        }
    });
    var FreightView = TemplateView.extend({ templateName: "#freight" });
    var SelectView = TemplateView.extend({ templateName: "#select" });
    var KombiView = TemplateView.extend({ templateName: "#kombi" });
    var HelpView = TemplateView.extend({ templateName: "#help" });
    var IndexView = TemplateView.extend({
        model: app.deliveries,
        templateName: "#deliveries",
        initialize: function(options) {
            TemplateView.prototype.initialize.apply(this,arguments);
            this.listenTo(this.model,"sync",this.render);
            this.model.fetch();
        },
        getContext: function() {
            return { deliveries: app.deliveries || null };
        },
    });
    var NavbarView = Backbone.View.extend({
        el: $('.menu-toggle'),
        events: {
            'click':'toggle',
        },
        toggle: function() {
            $('#wrapper').toggleClass('toggled');
        },
    });
    app.views.FreightView = FreightView;
    app.views.NavbarView = NavbarView;
    app.views.SelectView = SelectView;
    app.views.KombiView = KombiView;
    app.views.IndexView = IndexView;
    app.views.HelpView = HelpView;
})(jQuery, Backbone, _, app);
