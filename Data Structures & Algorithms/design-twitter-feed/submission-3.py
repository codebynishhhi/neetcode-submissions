from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):

        self.time = 0

        self.followMap = defaultdict(set)

        self.tweetMap = defaultdict(list)

    def postTweet(self, userId, tweetId):

        self.time += 1

        self.tweetMap[userId].append(
            (self.time, tweetId)
        )

    def follow(self, followerId, followeeId):

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):

        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

    def getNewsFeed(self, userId):

        heap = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:

            if self.tweetMap[followee]:

                index = len(self.tweetMap[followee]) - 1

                time, tweetId = self.tweetMap[followee][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, followee, index)
                )

        result = []

        while heap and len(result) < 10:

            negTime, tweetId, followee, index = heapq.heappop(heap)

            result.append(tweetId)

            if index > 0:

                index -= 1

                time, tweetId = self.tweetMap[followee][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, followee, index)
                )

        return result