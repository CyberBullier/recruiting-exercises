

### Richard's Solution for Deliverr Challenge
### Testing Instructions

Clone the repository locally
`git clone https://github.com/CyberBullier/recruiting-exercises.git`

Navigate to appropriate sub directory
`cd recruiting-exercises/inventory-allocator`
Run unnittests
`python3 -m unittest inventory_allocator_test.py `

### Food for thought?
- If we were to assume warehouses represented a modern database, we can update the database as we run our queries or wait until the client has recieved
a successful response. Without loss of generality, there are tradeoffs(think CAP theorem) one should make based on our contraints & system priotities.
