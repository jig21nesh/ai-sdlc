def get_invoice(invoices, invoice_id, actor_account):
    return next((i for i in invoices
                 if i['id'] == invoice_id and i['account'] == actor_account), None)
