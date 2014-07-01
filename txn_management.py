import nabcommerce

nab_instance=nabcommerce.Nabcommerce()

print "\n\n\n"

list_of_txns=nab_instance.query_transactions_families()
print "\n\n\n"

nab_instance.query_batch()
print "\n\n\n"

nab_instance.query_transactions_summary()
print "\n\n\n"

if list_of_txns and len(list_of_txns)>=1:
    txn_id=list_of_txns[0]["TransactionIds"][0]
    nab_instance.query_transactions_detail([txn_id])

print "Done"
