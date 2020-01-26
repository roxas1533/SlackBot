import requests
import os

headers = {"Authorization": "Bearer" + os.environ['Authorization']}


def run_query(query, variables):
    request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables},
                            headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query = """
query($name: String!){
  user(login: $name) {
    name
    email
    contributionsCollection(from: "2020-01-25T00:00:00", to: "2020-01-26T00:00:00") {
      totalRepositoryContributions
      totalCommitContributions
      commitContributionsByRepository {
        repository {
          nameWithOwner
        }
        contributions {
          totalCount
        }
      }
    }
  }
}
"""
variables = {
    "name": "roxas1533"
}
result = run_query(query, variables)
print(result)
count_commit = result["data"]["user"]["contributionsCollection"]["totalCommitContributions"]
print(count_commit)
