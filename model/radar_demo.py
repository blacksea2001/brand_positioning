# -*- coding: utf-8 -*- #
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')

# dimensions
name = [u'利率', u'額度', u'活動', u'APP', u'申辦']
# name = [u'LOAN', u'證券', u'基金', u'信用卡', u'外匯']

# 隨機數據
value1 = np.random.randint(50, 100, size=5) / 100
value2 = np.random.randint(40, 90, size=5) / 100
value3 = np.random.randint(30, 80, size=5) / 100

angles = np.linspace(0, 2*np.pi, len(name), endpoint=False)
angles = np.concatenate((angles, [angles[0]]))
value1 = np.concatenate((value1, [value1[0]]))
value2 = np.concatenate((value2, [value2[0]]))
value3 = np.concatenate((value3, [value3[0]]))

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, value1, 'o-', lw=1, label=u'大戶')
ax.fill(angles, value1, alpha=0.25)
ax.plot(angles, value2, 'o-', lw=1, label=u'A行')
ax.fill(angles, value2, alpha=0.25)
ax.plot(angles, value3, 'o-', lw=1, label=u'B行')
ax.fill(angles, value3, alpha=0.25)

ax.set_thetagrids(angles*180/np.pi, name)

# 雷達圖範圍
ax.set_ylim(0, 1.1)
ax.set_theta_zero_location('N')

#plt.title(u'口碑雷達圖', fontsize=20)
plt.legend(loc=1)
ax.grid(True)
plt.show()
