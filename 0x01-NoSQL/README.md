Introduction

This project focuses on exploring NoSQL databases, specifically MongoDB, and performing various database operations using Python and the pymongo library. The tasks involve creating, querying, updating, and managing MongoDB collections, along with some more advanced operations such as aggregation and handling indexes.
Files and Their Purpose

    8-all.py
        Purpose: Contains a function list_all that lists all documents in a specified MongoDB collection.

    9-insert_school.py
        Purpose: Contains a function insert_school that inserts a new document in a specified MongoDB collection.

    10-update_topics.py
        Purpose: Contains a function update_topics that updates the topics of a school document based on the name.

    11-schools_by_topic.py
        Purpose: Contains a function schools_by_topic that returns the list of school documents having a specific topic.

    12-log_stats.py
        Purpose: Provides statistics about Nginx request logs stored in a MongoDB collection. It prints the count of documents, the count of documents for each HTTP method, and the count of GET requests to the /status path.

    101-students.py
        Purpose: Contains a function top_students that returns all students sorted by their average score. Each student document includes an averageScore key.

    102-log_stats.py
        Purpose: Enhances the 12-log_stats.py script by adding a feature to display the top 10 most frequent IP addresses in the Nginx logs collection.

    101-main.py
        Purpose: Serves as the main script to demonstrate the usage of functions from other files. It inserts sample student documents, lists all students, and prints students sorted by their average score.

This project provides hands-on experience with NoSQL databases, specifically MongoDB, and demonstrates how to perform various database operations programmatically using Python. The tasks also emphasize understanding and implementing basic aggregation and data analysis within MongoDB.