# !/usr/bin/python
# coding:utf-8

from asterisk.ami import AMIClient

from  asterisk.ami import SimpleAction

def CallSip(exten,ponebind,callid):
    client = AMIClient(address='192.168.200.220', port=5060)
    client.login(username='6002', secret='pbx6002')
    sip = 'SIP/%s' % ponebind
    print(sip)
    action = SimpleAction(
        'Originate',
        Channel=sip,
        Exten=callid,  # 目标电话
        Priority=1,
        Context='MAIN_OUTGOING',  # 呼叫规则
        CallerID=exten,  # 来自电话
    )
    client.send_action(action)
    future = client.send_action(action)
    response = future.response

if __name__=="__main__":
    exten = '2100'
    ponebind = '2100'
    callid = '15209884564'
    CallSip(exten, ponebind, callid)