class Resources():
    """
        Class used to load add css and js resources to the page
    """
    js = []
    css = []
    
    def __init__(self):
        self.js = []
        self.css = []
    
    def addCss(self,filename):
        if filename not in self.css:
            self.css.append(filename)
        
    def addJs(self,filename):
        if filename not in self.js:
            self.js.append(filename)
        
    def getJsTags(self):
        tags = []
        for js in self.js:
            tag = '<script type="text/javascript" src="/static/js/%s" ></script>' % js 
            tags.append(tag)
        return tags
    
    def getCssTags(self):
        tags = []
        for css in self.css:
            tag = '<link rel="stylesheet" type="text/css" href="/static/css/%s" ></link>' % css 
            tags.append(tag)
        return tags
    
