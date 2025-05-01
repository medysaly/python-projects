# 🎬 Favorite Movies Tracker - Day 6 Mini Project

# Step 1: Collect favorite movies
movie_list = []

while len(movie_list) < 3:
    movie = input("What’s one of your favorite movies? ").strip().title()
    movie_list.append(movie)

# Step 2: Display the original list
print("\n🎥 Here’s your movie list:")
print(movie_list)

# Step 3: Sort the list alphabetically
movie_list.sort()
print("\n📚 Sorted list:")
print(movie_list)

# Step 4: Show how many movies are in the list
print(f"\n🎯 You have {len(movie_list)} movies in your list.")

# Step 5: Ask user to remove one movie
remove_item = input("\n❌ Which movie do you want to remove? ").strip().title()

if remove_item in movie_list:
    movie_list.remove(remove_item)
    print("\n✅ Here’s your updated list:")
    print(movie_list)
else:
    print("\n⚠️ That movie wasn't found in your list.")