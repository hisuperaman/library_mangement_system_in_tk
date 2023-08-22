def btnMouseEnter(btn):
    btn.config(bg='#675af4')
    btn.config(activebackground="#4e61da", activeforeground="white", cursor="hand2")

def btnMouseLeave(btn):
    btn.config(bg='#655bd6')

def pfpbtnMouseEnter(btn):
    btn.config(bg='#4e61da', fg='white')
    btn.config(activebackground="#4e61da", activeforeground="white", cursor="hand2")

def pfpbtnMouseLeave(btn):
    btn.config(bg='white', fg='#655bd6')