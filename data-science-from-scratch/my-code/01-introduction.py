# * Motivating Hypothetical: DataSciencester NOQA
from __future__ import division
from collections import Counter
from collections import defaultdict

# ** Finding Key Connectors
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
    {"id": 10, "name": "Jen"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Add a list of friends to each user
for user in users:
    user["friends"] = []

for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j])  # add i as a friend of j
    users[j]["friends"].append(users[i])  # add j as a friend of i


# Q - What's the average number of connections?
def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users)  # 24

num_users = len(users)  # 11
avg_connections = total_connections / num_users  # 2.2

# Q - Who are the most connected people?

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

sorted(num_friends_by_id, key=lambda pair: pair[1], reverse=True)

# ** Data Scientists You May Know


# Friend of friends
def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"] for friend in user["friends"]
            for foaf in friend["friends"]]


friends_of_friend_ids_bad(users[0])

users[0]["friends"]


# Produce a count of mutual friends
def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    """other_user is not a friend if he's not in user['friends'];
        that is, if he's not_the_same as all the people in
        user['friends']"""
    return all(not_the_same(friend, other_user) for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf) and not_friends(user, foaf))


friends_of_friend_ids(users[3])

# Finding users with a certain interest
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# Build a function that finds users with a certain interest
# Not the most efficient solution
def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

# user_ids_by_interest now represents a list of {interest: [id's...]}
# e.g
# 'Big Data': [0, 8, 9], 'C++': [5], ...
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Users to interests
# keys are user_ids, values are lists of interests for that user
interests_by_user_id = defaultdict(list)

# interests_by_user_id not represents a list of user_id: [interests..]
# e.g
# 0: ['Hadoop',
#  'Big Data',
#  'HBase',
#  'Java',
#  'Spark',
#  'Storm',
#  'Cassandra'], ...
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


# Q - Who has the most interests in common with a given user
def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])


# Call with users[int]
most_common_interests_with(users[4])

# ** Salaries and Experience
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Turn this into a fun fact

# Look at the average salary for each tenure

# keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# keys are years, each value is the average salary for that tenure
# e.g
# {0.7: 480000.0, ... }
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}


# Bucket the tenures
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# Group the salaries corresponding to each bucket


# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

# salary_by_tenure_bucket is now "bucket name": [salaries...]
# e.g
# 'between two and five': [60000, 63000]
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Compute the average salary for each group
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

# ** Topics of interest

# Q - Find the most popular interests
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
    