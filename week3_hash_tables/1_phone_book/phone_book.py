# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries: list[Query]) -> list[str]:
    """
    Process a list of queries. This function should:
        ∙ add number name. It means that the user adds a person with name name and phone number
            number to the phone book. If there exists a user with such number already, then your manager
            has to overwrite the corresponding name.
            
        ∙ del number. It means that the manager should erase a person with number number from the phone
            book. If there is no such person, then it should just ignore the query.

        ∙ find number. It means that the user looks for a person with phone number number. The manager
            should reply with the appropriate name, or with string “not found" (without quotes) if there is
            no such person in the book.
    Args:
        queries (list[Query]): List of queries to process
    
    Returns:
        list[str]: the responses for the "find" queries
    """
    results: list[str] = []
    contacts: list[str | None] = [None for i in range(int(10e6))] # dictionary comprehension for each number 0 to 10e7
    for q in queries:
        match q.type:
            case "add":
                contacts[q.number] = q.name
            case "find":
                result = contacts[q.number]
                if result != None:
                    results.append(result)
                else:
                    results.append("not found")
            case "del":
                if contacts[q.number] != None:
                    contacts[q.number] = None
                
    return results

def process_queries_(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

