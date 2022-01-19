# -*- Encoding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import numpy as np

# 반원 데이터 생성 - 붉은 반원, 푸른 반원으로 쪼개서 그리기
B = 7.5 + 7.5
L = 5 + 5
d = L / 2
r = d / 2
width = r
height = d/3  
angle0 = math.atan(2/3)
angle1 = math.degrees(angle0)

x1 = np.linspace(-math.sqrt(r * r * 9 / 13), r, 1000)
y1 = []
for i in x1:
    y1.append(math.sqrt((r * r) - (i * i)))
    
x2 = np.linspace(math.sqrt(r * r * 9 / 13), r, 1000)
y2 = []
for i in x2:
    y2.append(-math.sqrt((r * r) - (i * i)))
    
x_upper = list(x1) + list(x2)[::-1]
y_upper = list(y1) + list(y2)[::-1]

# 푸른 반원
x3 = np.linspace(-r, -math.sqrt(r * r * 9 / 13), 1000)
y3 = []
for i in x3:
    y3.append(math.sqrt((r * r) - (i * i)))
    
x4 = np.linspace(-r, math.sqrt(r * r * 9 / 13), 1000)
y4 = []
for i in x4:
    y4.append(-math.sqrt((r * r) - (i * i)))
    
x_lower = list(x3)[::-1] + list(x4)
y_lower = list(y3)[::-1] + list(y4)

# 3) 작은 원 데이터 생성
# - 붉은 원, 푸른 원 따로 생성
# - 원점을 중심으로 하는 작은 원을 생성한 뒤 좌표 이동하는 방식
# 푸른 원
x_little1 = np.linspace(-1.25, 1.25, 1000)
y_little_upper_1 = []
y_little_lower_1 = []
for i in x_little1:
    y_little_upper_1.append(math.sqrt((1.25 * 1.25) - (i * i)))
    y_little_lower_1.append(-math.sqrt((1.25 * 1.25) - (i * i)))
    
x_little1 = list(map(lambda x : x + (15 / (4 * math.sqrt(13))), x_little1))
y_little_upper_1 = list(map(lambda x : x + ((-2 / 3) * (15 / (4 * math.sqrt(13)))), y_little_upper_1))
y_little_lower_1 = list(map(lambda x : x + ((-2 / 3) *  (15 / (4 * math.sqrt(13)))), y_little_lower_1))

x_little1 = x_little1 + x_little1[::-1]
y_little1 = y_little_upper_1 + y_little_lower_1[::-1]

# 붉은 원
x_little2 = np.linspace(-1.25, 1.25, 1000)
y_little_upper_2 = []
y_little_lower_2 = []
for i in x_little2:
    y_little_upper_2.append(math.sqrt((1.25 * 1.25) - (i * i)))
    y_little_lower_2.append(-math.sqrt((1.25 * 1.25) - (i * i)))
    
x_little2 = list(map(lambda x : x - (15 / (4 * math.sqrt(13))), x_little2))
y_little_upper_2 = list(map(lambda x : x + ((2 / 3) * (15 / (4 * math.sqrt(13)))), y_little_upper_2))
y_little_lower_2 = list(map(lambda x : x + ((2 / 3) *  (15 / (4 * math.sqrt(13)))), y_little_lower_2))

x_little2 = x_little2 + x_little2[::-1]   
y_little2 = y_little_upper_2 + y_little_lower_2[::-1]

# 4) 그리기
# 도화지
fig, ax = plt.subplots()
fig.set_size_inches(15, 10)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim([-7.5, 7.5])
ax.set_ylim([-5, 5])

# 반원
ax.fill(x_lower, y_lower, '#144A9D')
ax.fill(x_upper, y_upper, '#D0303C')

# 작은 원
ax.fill(x_little1, y_little1, '#144A9D')
ax.fill(x_little2, y_little2, '#D0303C')

# 건곤감리
# Rectangle(xy, width, height, angle=0.0, fill=True, **kwargs)
# ax.plot([x_lower, y_lower], [x_upper, y_upper], transform=ax.transAxes)
# ax.plot([0, 1], [0, 1], transform=ax.transAxes)
# ax.plot([0, 1], [1, 0], transform=ax.transAxes)

# 5. 감(坎)
xy = [0,0]
move_goe_x = math.sqrt((d/4)**2 + (d/3)**2)
# print(f"{angle0=}", f"{angle1=}", end=" => ")
# print(f"{math.cos(angle0)=}", end=" vs. ")
# print(f"{math.cos(angle1)=}")
xy[0] =  move_goe_x
xy[0] = xy[0] + (1 + 1/2)*r*math.cos(angle0) 
xy[1] = xy[1] + (1 + 1/2)*r*math.sin(angle0) 
ax.add_patch(patches.Rectangle(xy, width, height, angle = angle1+90, edgecolor = 'white', facecolor = 'black', fill=True))
gam_xy = xy

xy[0] = xy[0] - (1/6)*r*math.cos(angle0) 
xy[1] = xy[1] - (1/6)*r*math.sin(angle0)
ax.add_patch(patches.Rectangle(xy, width+0.1, r/12, angle = angle1+90, edgecolor = 'white', facecolor = 'white', fill=True))

xy[0] = xy[0] - (1/6+2/24)*r*math.cos(angle0)
xy[1] = xy[1] - (1/6+2/24)*r*math.sin(angle0)
ax.add_patch(patches.Rectangle(xy, width+0.2, r/12, angle = angle1+90, edgecolor = 'white', facecolor = 'white', fill=True))

xy[0] = xy[0] - (1/6+1/12+1/24)*r*math.cos(angle0)
xy[1] = xy[1] + (3/6+2/12-1/24)*r*math.sin(angle0)
# ax.add_patch(patches.Rectangle(xy, r/12+0.2, r/12, angle = angle1, edgecolor = 'blue', facecolor = 'white', fill=True))
gam_add2 = xy

xy[0] = xy[0] + (1/6+1/12)*r*math.cos(angle0)
xy[1] = xy[1] + (1/6+1/12)*r*math.sin(angle0)
ax.add_patch(patches.Rectangle(xy, r/12+0.4, r/12, angle = angle1, edgecolor = 'white', facecolor = 'white', fill=True))

xy = gam_add2
xy[0] = xy[0] - 2*(1/6+1/12)*r*math.cos(angle0)
xy[1] = xy[1] - 2*(1/6+1/12)*r*math.sin(angle0)
ax.add_patch(patches.Rectangle(xy, r/12+0.4, r/12, angle = angle1, edgecolor = 'white', facecolor = 'white', fill=True))

# 3. 건(乾)
xy = [0,0]
move_goe_x = r/2*math.cos(math.pi/2 - angle0)
move_goe_y = r/2*math.sin(math.pi/2 - angle0)
# print(f"{move_goe_x=}", f"{ move_goe_y=}")

xy = [0,0]
xy[0] = xy[0] - (r + r*1/2 + r/12) * math.cos(angle0) - move_goe_x
xy[1] = xy[1] + (r + r*1/2 + r/12) * math.sin(angle0) - move_goe_y
ax.add_patch(patches.Rectangle(xy, width, height, angle = 90-angle1, edgecolor = 'white', facecolor = 'black', fill=True))

xy[0] = xy[0] - (3/12+1/24)*r*math.cos(math.pi/2 - angle0) 
xy[1] = xy[1] + (1/12)*r*math.sin(math.pi/2 - angle0)
ax.add_patch(patches.Rectangle(xy, width+0.1, r/12, angle = 90-angle1, edgecolor = 'white', facecolor = 'white', fill=True))

xy[0] = xy[0] - (5/12-1/24)*r*math.cos(math.pi/2 - angle0)
xy[1] = xy[1] + (2/12-1/24+1/48)*r*math.sin(math.pi/2 - angle0)
ax.add_patch(patches.Rectangle(xy, width+0.2, r/12, angle = 90-angle1, edgecolor = 'white', facecolor = 'white', fill=True))

# 6. 곤(坤)
xy = [0,0]
move_goe_x = r/2*math.cos(math.pi/2 - angle0)
move_goe_y = r/2*math.sin(math.pi/2 - angle0)
# print(f"{move_goe_x=}", f"{ move_goe_y=}")

xy = [0,0]
xy[0] = xy[0] + (2*r + r/6) * math.cos(angle0) - move_goe_x
xy[1] = xy[1] - (2*r + r/6) * math.sin(angle0) - move_goe_y
ax.add_patch(patches.Rectangle(xy, width, height, angle = 90-angle1, edgecolor = 'white', facecolor = 'black', fill=True))

xy[0] = xy[0] - (13/48)*r*math.cos(math.pi/2 - angle0) 
xy[1] = xy[1] + (1/12)*r*math.sin(math.pi/2 - angle0)
ax.add_patch(patches.Rectangle(xy, width+0.1, r/12, angle = 90-angle1, edgecolor = 'white', facecolor = 'white', fill=True))

xy[0] = xy[0] - (9/24)*r*math.cos(math.pi/2 - angle0)
xy[1] = xy[1] + (1/6)*r*math.sin(math.pi/2 - angle0)
ax.add_patch(patches.Rectangle(xy, width+0.2, r/12, angle = 90-angle1, edgecolor = 'white', facecolor = 'white', fill=True))

xy = [0,0]
xy[0] = xy[0] + (2 + 2/6+1/6+1/12)*r*math.cos(angle0) - move_goe_x
xy[1] = xy[1] - (1 + 1/6+1/6+1/12)*r*math.sin(angle0) - move_goe_y
ax.add_patch(patches.Rectangle(xy, 7*r/12+0.4, r/12, angle = 180-angle1, edgecolor = 'white', facecolor = 'white', fill=True))

# 4. 리(離)
move_goe_x = r/2*math.cos(math.pi/2 - angle0)
move_goe_y = r/2*math.sin(math.pi/2 - angle0)
xy = [0,0]
xy[0] = xy[0] - (r + r*1/2 + r/12) * math.cos(angle0) + move_goe_x
xy[1] = xy[1] - (r + r*1/2 + r/12) * math.sin(angle0) - move_goe_y
ax.add_patch(patches.Rectangle(xy, width, height, angle = angle1+90, edgecolor = 'white', facecolor = 'black', fill=True))

xy[0] = xy[0] - (1/6-1/24+1/24-1/48)*r*math.cos(angle0) 
xy[1] = xy[1] - (1/6+1/24+1/24-1/48)*r*math.sin(angle0)
ax.add_patch(patches.Rectangle(xy, width+0.1, r/12, angle = angle1+90, edgecolor = 'white', facecolor = 'white', fill=True))

xy[0] = xy[0] - (1/6+1/24+1/48)*r*math.cos(angle0)
xy[1] = xy[1] - (1/6+2/24+1/48)*r*math.sin(angle0)
ax.add_patch(patches.Rectangle(xy, width+0.2, r/12, angle = angle1+90, edgecolor = 'white', facecolor = 'white', fill=True))

xy[0] = xy[0] - (1/6+2/12+1/24)*r*math.cos(angle0)
xy[1] = xy[1] + (3/6+6/24)*r*math.sin(angle0)
ax.add_patch(patches.Rectangle(xy, r/12+0.3, r/12, angle = angle1, edgecolor = 'white', facecolor = 'white', fill=True))

plt.savefig('Steven\'s Taegeug-gi_final.png')
plt.show()
