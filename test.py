import btcutils

res = btcutils.check_merkle_branch("00000000000000001c7d7de14a86a03801b2d94c729b029a755eea950be94f90", [ 'aaa','bbb','ccc' ], 2)

print res
