import csv
import sys
import matplotlib.pyplot as plt 

def main():
	if len(sys.argv) < 2:
		print('Must supply name of the fight song csv file.')
		return

	songs, conferences = GetSongData(sys.argv[1])
	years = GetYears(songs)
	song_introductions = GetSongByConference(songs, conferences)
	DoPlot(song_introductions, years)

def DoPlot(song_introductions, years):
	for conference in sorted(song_introductions.keys()):
		plt.plot(years, song_introductions[conference], alpha=0.5, linewidth=3, label=conference)
	plt.legend(loc='lower right')
	plt.title('Number of Fight Songs By Year and Conference')
	plt.xlabel('Year')
	plt.ylabel('Number')
	plt.show()  

def GetSongByConference(songs, conferences):
	"""	This function pulls data from the compound dictionary and builds
		a single list containing the number of songs introduced in every year
		one for each conference (which is a dictionary key).
	"""
	song_intros = {}
	for conference in conferences:
		song_intros[conference] = []
		cumulative_count = 0
		for year in songs.keys():
			if conference in songs[year]:
				cumulative_count += songs[year][conference]
			song_intros[conference].append(cumulative_count)
	return song_intros

def GetYears(songs):
	"""	This function simply returns the keys in the songs dictionary as a list.
	"""
	return list(songs.keys())

def GetSongData(filename):
	"""	GetSongData(filename)
	
		This function attempts to open the given file as a fivethirtyeight fight song csv file.
		The file contains data on the fight song for each team in several major collegiate sports
		conferences. Our aim is to produce a stackplot comparing new song introduction by year.

		songs[year][conference] = count
		conferences = set(conference)
	"""
	file_in = open(filename, 'r')
	reader = csv.DictReader(file_in)
	songs = {}
	conferences = set()
	# Ensure every year is represented.
	for year in range(1880, 1971):
		songs[year] = {}
	# Counter initialized to 1 due to headings.
	counter = 1
	for line in reader:
		counter += 1
		# Don't allow an 'Unknown' to cause a crash.
		if line['year'] == 'Unknown':
			print('Line {:d} [{:s}] skipped due to unknown year'.format(counter, line['school']))
			continue
		conferences.add(line['conference'])
		year = int(line['year'])
		if line['conference'] in songs[year]:
			songs[year][line['conference']] += 1
		else:
			songs[year][line['conference']] = 1
	return songs, conferences

if __name__ == '__main__':
	main()

