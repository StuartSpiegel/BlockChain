#We have a format for our requests but we need to add them
#as a node in the blockchain, we create an HTTP server
#so anyone can notify the blockchain that a transaction
#has occured.
# [Node] --> accepts POST REQUEST
#This is the purpose for formatting our requests in JSON format
#The data has to be able to reach the server in a deliverable format (REQUEST).


from flask import Flask
from flask import request
node = Flask(__name__)

# Store the transaction of this node in a list
this_nodes_transactions = []

@node.route('/txion', methods=['POST'])
def transaction():
  if request.method == 'POST':
    # On each new POST request,
    # we extract the transaction data
    new_txion = request.get_json()
    # Then we add the transaction to our list
    this_nodes_transactions.append(new_txion)
    # Because the transaction was successfully
    # submitted, we log it to our console
    print "New transaction"
    print "FROM: {}".format(new_txion['from'])
    print "TO: {}".format(new_txion['to'])
    print "AMOUNT: {}\n".format(new_txion['amount'])
    # Notify the client of a succsessful submission 
    return "Transaction submission successful\n"

node.run()
