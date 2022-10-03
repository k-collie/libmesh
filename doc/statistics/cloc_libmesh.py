#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math

# Import stuff for working with dates
from datetime import datetime
from matplotlib.dates import date2num

# git checkout `git rev-list -n 1 --before="$my_date" master`
# cloc.pl src/*/*.C include/*/*.h

data = [
# 2003 - All data from archived svn repo
    # '2003-01-10', 158, 29088, # SVN revision 4 - this is the first revision with trunk/libmesh
    # '2003-01-20', 184, 28937, # SVN revision 11
    # '2003-01-24', 198, 31158, # SVN revision 23
    '2003-02-04', 198, 31344, # SVN revision 47
    '2003-03-04', 243, 36036,
    '2003-04-04', 269, 39946,
    '2003-05-04', 275, 40941,
    '2003-06-04', 310, 44090,
    '2003-07-04', 319, 44445,
    '2003-08-04', 322, 45225,
    '2003-09-04', 325, 46762,
    '2003-10-04', 327, 47151,
    '2003-11-04', 327, 47152, # Up to now, all the include files were in the same directory
    '2003-12-04', 327, 47184,
# 2004 - All data from archived svn repo
    '2004-01-04', 339, 48437,
    '2004-02-04', 343, 50455,
    '2004-03-04', 347, 52198,
    '2004-04-04', 358, 52515,
    '2004-05-04', 358, 52653,
    '2004-06-04', 369, 53953,
    '2004-07-04', 368, 53981,
    '2004-08-04', 371, 54316,
    '2004-09-04', 371, 54510,
    '2004-10-04', 375, 55785,
    '2004-11-04', 375, 55880,
    '2004-12-04', 384, 56612,
# 2005 - All data from archived svn repo
    '2005-01-04', 385, 56674,
    '2005-02-04', 406, 61034,
    '2005-03-04', 406, 62423,
    '2005-04-04', 403, 62595,
    '2005-05-04', 412, 63540,
    '2005-06-04', 416, 69619,
    '2005-07-04', 425, 72092,
    '2005-08-04', 425, 72445,
    '2005-09-04', 429, 74148,
    '2005-10-04', 429, 74263,
    '2005-11-04', 429, 74486,
    '2005-12-04', 429, 74629,
# 2006 - All data from archived svn repo
    '2006-01-04', 429, 74161,
    '2006-02-04', 429, 74165,
    '2006-03-04', 429, 74170,
    '2006-04-04', 429, 74864,
    '2006-05-04', 433, 73847,
    '2006-06-04', 438, 74681,
    '2006-07-04', 454, 76954,
    '2006-08-04', 454, 77464,
    '2006-09-04', 454, 77843,
    '2006-10-04', 454, 78051,
    '2006-11-04', 463, 78683,
    '2006-12-04', 463, 79057,
# 2007 - All data from archived svn repo
    '2007-01-04', 463, 79149,
    '2007-02-04', 475, 79344,
    '2007-03-04', 479, 81416,
    '2007-04-04', 479, 81468,
    '2007-05-04', 481, 84312,
    '2007-06-04', 481, 85565,
    '2007-07-04', 482, 85924,
    '2007-08-04', 485, 86248,
    '2007-09-04', 487, 86481,
    '2007-10-04', 497, 87926,
    '2007-11-04', 502, 89687,
    '2007-12-04', 512, 93523,
# 2008 - All data from archived svn repo
    '2008-01-04', 512, 94263,
    '2008-02-04', 515, 94557,
    '2008-03-04', 526, 98127,
    '2008-04-04', 526, 98256,
    '2008-05-04', 531, 99715,
    '2008-06-04', 531, 99963,
    '2008-07-04', 538, 100839,
    '2008-08-04', 542, 101682,
    '2008-09-04', 548, 102163,
    '2008-10-04', 556, 104185,
    '2008-11-04', 558, 104535,
    '2008-12-04', 565, 106318,
# 2009 - All data from archived svn repo
    '2009-01-04', 565, 106340,
    '2009-02-04', 579, 108431,
    '2009-03-04', 584, 109050,
    '2009-04-04', 584, 109922,
    '2009-05-04', 589, 110821,
    '2009-06-04', 591, 111094,
    '2009-07-04', 591, 111571,
    '2009-08-04', 591, 111555,
    '2009-09-04', 591, 111746,
    '2009-10-04', 591, 111920,
    '2009-11-04', 595, 112993,
    '2009-12-04', 597, 113744,
# 2010 - All data from archived svn repo
    '2010-01-04', 598, 113840,
    '2010-02-04', 600, 114378,
    '2010-03-04', 602, 114981,
    '2010-04-04', 603, 115509,
    '2010-05-04', 603, 115821,
    '2010-06-04', 603, 115875,
    '2010-07-04', 627, 126159,
    '2010-08-04', 627, 126217,
    '2010-09-04', 628, 126078,
    '2010-10-04', 642, 129417,
    '2010-11-04', 643, 130045,
    '2010-12-04', 648, 131363,
# 2011 - All data from archived svn repo
    '2011-01-04', 648, 131644,
    '2011-02-04', 648, 132105,
    '2011-03-04', 658, 132950,
    '2011-04-04', 661, 133643,
    '2011-05-04', 650, 133958,
    '2011-06-04', 662, 134447,
    '2011-07-04', 667, 134938,
    '2011-08-04', 679, 136338,
    '2011-09-04', 684, 138165,
    '2011-10-04', 686, 138627,
    '2011-11-04', 690, 141876,
    '2011-12-04', 690, 142096,
# 2012
    '2012-01-04', 694, 142345,
    '2012-02-04', 697, 142585,
    '2012-03-04', 703, 146127,
    '2012-04-04', 706, 147191,
    '2012-05-04', 708, 148202,
    '2012-06-04', 705, 148334,
    '2012-07-04', 713, 150066,
    '2012-08-04', 727, 152269,
    '2012-09-04', 725, 152381,
    '2012-10-04', 734, 155213, # cloc reports 1092 and 1094 files for Oct/Nov, Don't know what happened...
    '2012-11-04', 743, 156082, # We moved from libmesh/src to src around here so maybe that caused it?
    '2012-12-04', 752, 156903,
# 2013
    '2013-01-04', 754, 158689, # 8f3e4977
    '2013-02-04', 770, 161001, # f495444d
    '2013-03-04', 776, 162239, # a7db13bb
    '2013-04-04', 783, 162986, # bcb7ede1
    '2013-05-04', 785, 163808, # 1f8be16b
    '2013-06-04', 785, 164022, # bb96e8a6
    '2013-07-04', 789, 163854, # 6651e65b
    '2013-08-04', 789, 164269, # ee336c6d
    '2013-09-04', 790, 165129, # bd37bb54
    '2013-10-04', 790, 165447, # 36341107
    '2013-11-04', 792, 166342, # eb1a1b7d
    '2013-12-04', 794, 168812, # 474509c0
# 2014
    '2014-01-04', 796, 170174, # f7e9b2a2
    '2014-02-04', 796, 170395, # a93acc24
    '2014-03-04', 799, 172037, # 799c3521
    '2014-04-04', 801, 172230, # 46974589
    '2014-05-04', 806, 173772, # 66d4e144
    '2014-06-04', 807, 171098, # e437059d
    '2014-07-04', 807, 171220, # 86e6540c
    '2014-08-04', 808, 172534, # 3b5bb943
    '2014-09-04', 808, 173694, # ef4465a5
    '2014-10-04', 819, 175750, # eedbf7b3
    '2014-11-04', 819, 176415, # c9675dcc
    '2014-12-04', 819, 176277, # c3b2bc9f
# 2015
    '2015-01-04', 819, 176289, # 18abbe4d
    '2015-02-04', 824, 176758, # 1034fe81
    '2015-03-04', 825, 176958, # 54bc2d27
    '2015-04-04', 830, 176926, # c9451c01
    '2015-05-04', 826, 176659, # e9e008a6
    '2015-06-04', 835, 178411, # 5f771ed6
    '2015-07-04', 840, 179578, # ea34669e
    '2015-08-04', 844, 180953, # eb301034
    '2015-09-04', 846, 181675, # ddab3b52
    '2015-10-04', 849, 181196, # 6d36bc77
    '2015-11-04', 848, 181385, # acc4cc5b
    '2015-12-04', 849, 180331, # f434f93f
# 2016
    '2016-01-04', 849, 180538, # 0de29508
    '2016-02-04', 846, 182937, # 04b618f4
    '2016-03-04', 846, 182727, # f63ac0b8
    '2016-04-04', 849, 183261, # a59cce15
    '2016-05-04', 849, 183176, # 4c78b30b
    '2016-06-04', 853, 184649, # 3393e1a9
    '2016-07-04', 839, 183363, # ead29425
    '2016-08-04', 837, 183288, # 8406aac3
    '2016-09-04', 842, 183850, # 1bf9f548
    '2016-10-04', 848, 185062, # 72f8aa7d
    '2016-11-04', 850, 185408, # 3a90559b
    '2016-12-04', 853, 185683, # 4636ea58
# 2017
    '2017-01-04', 853, 185885, # 6c7743ee
    '2017-02-04', 853, 186246, # be0ecd40
    '2017-03-04', 850, 184993, # 7913dc77
    '2017-04-04', 856, 185905, # 1e5cb6f6
    '2017-05-04', 855, 186311, # dfd89fe6
    '2017-06-04', 855, 186441, # 642b81d3
    '2017-07-04', 856, 186664, # 586e9751
    '2017-08-04', 856, 186707, # 5a6642bf
    '2017-09-04', 856, 186793, # d75605cb
    '2017-10-04', 856, 187219, # b291e377
    '2017-11-04', 861, 186893, # 4d08770f
    '2017-12-04', 863, 187335, # 7e8c93f0
# 2018
    '2018-01-04', 862, 186607, # 0a86a3c1
    '2018-02-04', 862, 186902, # 158829d4
    '2018-03-04', 862, 187127, # 3287318f
    '2018-04-04', 862, 186557, # 0dcfe02f
    '2018-05-04', 879, 186594, # ad06819b
    '2018-06-04', 880, 186738, # bfa9b7a3
    '2018-07-04', 882, 189018, # 92c9b163
    '2018-08-04', 884, 189659, # fee809be
    '2018-09-04', 884, 190046, # bd3db5ba
    '2018-10-04', 886, 190239, # b7c021ef
    '2018-11-04', 886, 190164, # b68a3414
    '2018-12-04', 886, 190650, # 3134aa86
# 2019
    '2019-01-04', 886, 191341, # 08ea2d6d
    '2019-02-04', 879, 189708, # 3679dac7
    '2019-03-04', 879, 190253, # 0a047066
    '2019-04-04', 879, 190583, # 260d091f
    '2019-05-04', 880, 192048, # c4c9fd54
    '2019-06-04', 880, 192174, # 49e6d8fa
    '2019-07-04', 885, 192442, # 5469d454
    '2019-08-04', 886, 191947, # e3f7c8e2
    '2019-09-04', 893, 194600, # 2d7cfaac
    '2019-10-04', 898, 195670, # d252e82f
    '2019-11-04', 899, 195840, # bd0812c7
    '2019-12-04', 896, 191898, # ac649146
# 2020
    '2020-01-04', 900, 192704, # 259ad8f4
    '2020-02-04', 900, 193538, # 3d4ec1c6
    '2020-03-04', 901, 194935, # 56ffd2f6
    '2020-04-04', 904, 196199, # 9ac9b4b9
    '2020-05-04', 904, 196658, # 6e32c593
    '2020-06-04', 904, 197092, # f707c65a
    '2020-07-04', 905, 197773, # b9d342ba
    '2020-08-04', 906, 198400, # cb8514e3
    '2020-09-04', 906, 198749, # 1630a53b
    '2020-10-04', 907, 199497, # e9c15910
    '2020-11-04', 909, 200385, # 4825db9c
    '2020-12-04', 909, 200392, # 7a6d338b
# 2021
    '2021-01-04', 909, 200705, # 3b410bcf
    '2021-02-04', 911, 201006, # 0c89409c
    '2021-03-04', 913, 201897, # d95eef7b
    '2021-04-04', 913, 202506, # 5298bf63
    '2021-05-04', 914, 204952, # 27b4a43d
    '2021-06-04', 914, 205061, # 16dff2ff
    '2021-07-04', 918, 205622, # 5fcbf3ae
    '2021-08-04', 918, 205957, # a0f5f800
    '2021-09-04', 918, 206599, # 213f1047
    '2021-10-04', 923, 209158, # 8b0c446c
    '2021-11-04', 923, 210630, # 6efe68bc
    '2021-12-04', 929, 211431, # 7db4373a
# 2022
    '2022-01-04', 931, 211714, # c1897db0
    '2022-02-04', 935, 212387, # 30237b84
    '2022-03-04', 936, 213559, # 172f5708
    '2022-04-04', 936, 213760, # e2bf5733
    '2022-05-04', 936, 214529, # f48e169b
    '2022-06-04', 936, 215737, # 4747096d
    '2022-07-04', 936, 215719, # 97fafb9c
    '2022-08-04', 936, 216199, # 7bfdc320
    '2022-09-04', 936, 215157, # ca67cb4f
]

# Extract the dates from the data array
date_strings = data[0::3]

# Convert date strings into numbers
date_nums = []
for d in date_strings:
  date_nums.append(date2num(datetime.strptime(d, '%Y-%m-%d')))

# Extract number of files from data array
n_files = data[1::3]

# Extract number of lines of code from data array
n_lines = data[2::3]

# Get a reference to the figure
fig = plt.figure()

# add_subplot(111) is equivalent to Matlab's subplot(1,1,1) command.
# The colors used come from sns.color_palette("muted").as_hex(). They
# are the "same basic order of hues as the default matplotlib color
# cycle but more attractive colors."
# We use the twinx() command to add a second y-axis
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

# We use the grid lines from the second axis (lines of code) as I think
# that is generally of more interest than number of files. I ran into
# an issue using axis='both', but turning on the x-grid on ax1 and the
# y-grid on ax2 seems to do the trick.

# According to this SO, we can force the grid lines to be displayed "below"
# the data using these flags, but this did not work for me.
# https://stackoverflow.com/questions/1726391/matplotlib-draw-grid-lines-behind-other-graph-elements
ax1.set_axisbelow(True)
ax2.set_axisbelow(True)

ax1.grid(b=True, axis='x', color='lightgray', linestyle='--', linewidth=1, alpha=0.25)
ax2.grid(b=True, axis='y', color='lightgray', linestyle='--', linewidth=1, alpha=0.25)

# Plot number of files vs. time
ax1.plot(date_nums, n_files, color=u'#4878cf', marker='o', linestyle='-', markersize=4, markevery=5)
ax1.set_ylabel('Files (blue circles)')

# Set up x-tick locations
ticks_names = ['2003', '2005', '2007', '2009', '2011', '2013', '2015', '2017', '2019', '2021']

# Get numerical values for the names
tick_nums = []
for x in ticks_names:
  tick_nums.append(date2num(datetime.strptime(x + '-03-04', '%Y-%m-%d')))

# Set tick labels and positions
ax1.set_xticks(tick_nums)
ax1.set_xticklabels(ticks_names)

# Plot lines of code vs. time
ax2.plot(date_nums, np.divide(n_lines, 1000.), color=u'#6acc65', marker='s', linestyle='-', markersize=4, markevery=5)
ax2.set_ylabel('Lines of code in thousands (green squares)')

# Trying to get the grid lines "under" the data using the method described here:
# https://stackoverflow.com/questions/1726391/matplotlib-draw-grid-lines-behind-other-graph-elements
# but this does not seem to have any effect no matter what number I use.
# [line.set_zorder(10) for line in ax1.lines]
# [line.set_zorder(10) for line in ax2.lines]

# Create linear curve fits of the data
files_fit = np.polyfit(date_nums, n_files, 1)
lines_fit = np.polyfit(date_nums, n_lines, 1)

# Convert to files/month
files_per_month = files_fit[0]*(365./12.)
lines_per_month = lines_fit[0]*(365./12.)

# Print curve fit data on the plot , '%.1f'
# files_msg = 'Approx. ' + '%.1f' % files_per_month + ' files added/month'
# lines_msg = 'Approx. ' + '%.1f' % lines_per_month + ' lines added/month'
# ax1.text(date_nums[len(date_nums)/4], 300, files_msg);
# ax1.text(date_nums[len(date_nums)/4], 250, lines_msg);

# Save as PDF
plt.savefig('cloc_libmesh.pdf', format='pdf')

# Local Variables:
# python-indent: 2
# End:
