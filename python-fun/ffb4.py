# Chapter 5

taylor_2020 = {
    'name': 'Jonathan Taylor',
    'rushing_yds': 1169
}

taylor_2020['rushing_tds'] = 11
# print(taylor_2020)

rec_yds = taylor_2020.get('rec_yds', 'byah')
catches = taylor_2020.get('catches', 0)
# print(rec_yds)
# print(catches)

for k, v in taylor_2020.items():
    print('{0}: {1}'.format(k, v))

# print(taylor_2020.items())

