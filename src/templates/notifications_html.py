# Autogenerated file
def render(info, services, notifications):
    yield """
    <table cellpadding='4' border='1' frame='box' rules='all'>
       <TH>
       <TH>ID
       <TH>Service
       <TH>Server
       <TH>Port
       <TH>Enabled
       <TH>
       """
    for notification in notifications:
        yield """
           """
        if notification['id'] != 0:
            yield """ 
               <TR>
                  <TD><a class=\"button link\" href=\"/notification_setting?id="""
            yield str(notification['id'])
            yield """\">Edit</a>
                  <TD>"""
            yield str(notification['id'])
            yield """
               """
            for service in services:
                yield """
                  """
                if notification['serviceid'] == service['id']:
                    yield """ 
                  <TD>"""
                    yield str(service['name'])
                    yield """
                  <TD>"""
                    yield str(service['server'])
                    yield """
                  <TD>"""
                    yield str(service['port'])
                    yield """
                  """
                yield """
               """
            yield """
                  <TD><span style=\"color:"""
            if notification['enable']:
                yield """green"""
            else:
                yield """red"""
            yield """\">"""
            if notification['enable']:
                yield """Yes"""
            else:
                yield """No"""
            yield """</span>
                  <TD><a class=\"button link\" href=\"/notification_setting?id="""
            yield str(notification['id'])
            yield """&oper=del\">Del</a>
           """
        yield """
       """
    yield """
       <TR>
          <TD><a class=\"button link\" href=\"/notification_setting?id=0\">Add</a>
          <TD colspan=\"6\">
    </table>
"""
