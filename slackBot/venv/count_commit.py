import requests
import os
import datetime
import tweetCommit as tw

headers = {"Authorization": "Bearer " + os.environ['Authorization']}


class CC:
    def run_query(self, query, variables):
        request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables},
                                headers=headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

    # The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
    query = """
    query($name: String!,$from: DateTime!,$to:DateTime!){
      user(login: $name) {
        name
        email
        contributionsCollection(from: $from, to: $to) {
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
        "name": "roxas1533",
        "to": "{0:%Y-%m-%dT}00:00:00".format(datetime.datetime.now().date()),
        "from": "{0:%Y-%m-%dT}00:00:00".format((datetime.datetime.now() - datetime.timedelta(days=1)).date())
    }

    def startCount(self):
        result = self.run_query(self.query, self.variables)
        print(result)
        count_commit = result["data"]["user"]["contributionsCollection"]["totalCommitContributions"]
        tw.tweet("@k365990900\n今日のコミットは{}でした".format(count_commit))
