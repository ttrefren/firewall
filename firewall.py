from django.template import Context, Template

def generate_iptables(filename, ips):
    """
        Generate iptables files from templates.
    """
    path = os.path.dirname(__file__)
    f = open('%s/templates/%s' % (path, filename))
    f = ''.join([line for line in f])
    t = Template(f)    
    c = Context({ 'servers': ips })
    rendered = t.render(c)

    out = open('%s/rendered/%s' % (path, filename), 'w')
    out.write(rendered)