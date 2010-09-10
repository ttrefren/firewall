from django.template import Context, Template
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

def generate_iptables(filename, ips):
    """
        Generate iptables files from templates.
    """
    f = open('templates/%s' % filename)
    f = ''.join([line for line in f])
    t = Template(f)    
    c = Context({ 'servers': ips })
    rendered = t.render(c)

    out = open('rendered/%s' % filename, 'w')
    out.write(rendered)

if __name__ == "__main__":
    generate_iptables('iptables.int.rules', ['1.1.1.1', '2.2.2.2'])
