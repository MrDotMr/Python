import random, time

out = open('二舍B243 '+ time.strftime('%Y{y}%m{m}%d{d}').format(y='-', m='-', d=' ')+'体温记录.txt', 'w')
out.write('疫情就是命令！防控就是责任！\n坚决打赢疫情防控攻坚战、阻击战、总体战！\n\n二舍B243 '+ time.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日') + ' 体温记录\n')
for per in {'郭永亮', '徐超', '张展鹏', '张昱'}:
    out.write(per + '\t' + str(round(random.uniform(36, 37.3), 1)) + '度\n')
out.close()
