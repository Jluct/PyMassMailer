class TemplateEngine:
    engine = ''

    def __init__(self, engine):
        self.engine = engine

    def render(self, tpl, data=''):
        template = self.engine(tpl)
        return template.render(data)
