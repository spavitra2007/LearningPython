import numpy as np
names=["pavitra", "subbu", "kavi", "shivani"]
marks=[20,56,78,89]
scores=np.array(marks)
print("\n📋 Student Scores (NumPy Array):")
print("   np.array(marks) →", scores)
print("   Type            :", type(scores)) 
average  = np.mean(scores)    # add all, divide by count
highest  = np.max(scores)     # largest number
lowest   = np.min(scores)     # smallest number
total    = np.sum(scores)     # sum of everything
spread   = np.std(scores)     # standard deviation (how spread marks are)
print("\n📊 Class Statistics:")
print(f"   np.mean(scores)  → Average  : {average:.2f}")
print(f"   np.max(scores)   → Highest  : {highest}")
print(f"   np.min(scores)   → Lowest   : {lowest}")
print(f"   np.sum(scores)   → Total    : {total}")
print(f"   np.std(scores)   → Std Dev  : {spread:.2f}")

passed_scores = scores[scores >= 40]   # only scores that are 40 or above
failed_scores = scores[scores <  40]   # only scores below 40

print("\n✅ Passed Students:")
print("   scores[scores >= 40] →", passed_scores)
print("   Number who passed    :", len(passed_scores))
print("\n❌ Failed Students:")
print("   scores[scores < 40]  →", failed_scores)
print("   Number who failed    :", len(failed_scores))
 

bonus_scores  = scores + 5          # give every student +5 bonus marks
doubled       = scores * 2          # double every score (just for demo)
percentage    = (scores / 100) * 100 
print("\n🎁 Bonus Marks (+5 added to everyone):")
print("   scores + 5 →", bonus_scores)
print("   (No loop needed — NumPy does it to ALL at once!)")

def get_grade(score):
    if score >= 90: return "A"
    elif score >= 75: return "B"
    elif score >= 60: return "C"
    elif score >= 40: return "D"
    else: return "F"
grades = [get_grade(s) for s in scores]

print("\n" + "=" * 55)
print("               📄 FULL REPORT CARD")
print("=" * 55)
print(f"{'Name':<10} {'Score':>6} {'Grade':>6} {'Status':>8}")
print("-" * 35)

for i in range(len(names)):
    status = "PASS ✅" if scores[i] >= 40 else "FAIL ❌"
    print(f"{names[i]:<10} {scores[i]:>6} {grades[i]:>6} {status:>8}")


print("-" * 35)
print(f"{'Class Avg':<10} {average:>6.1f}")

top_index  = np.argmax(scores)   # index of highest score
low_index  = np.argmin(scores)   # index of lowest score

print("\n🏆 Top Scorer    :", names[top_index],  "→", scores[top_index])
print("📉 Needs Help    :", names[low_index],  "→", scores[low_index])

sorted_asc  = np.sort(scores)           # low to high
sorted_desc = np.sort(scores)[::-1]     # high to low (reverse)

print("\n📈 Scores Low → High :", sorted_asc)
print("📉 Scores High → Low :", sorted_desc)

above_avg_mask  = scores > average               # True/False for each student
above_avg_names = [names[i] for i, v in enumerate(above_avg_mask) if v]
above_avg_scores = scores[above_avg_mask]

print(f"\n⭐ Students Above Average ({average:.1f}):")
for n, s in zip(above_avg_names, above_avg_scores):
    print(f"   {n} → {s}")

print("\n" + "=" * 55)
print("   NumPy Functions Used in This Project:")
print("=" * 55)
print("   np.array()     → Create a NumPy array from a list")
print("   np.mean()      → Calculate the average")
print("   np.max()       → Find the highest value")
print("   np.min()       → Find the lowest value")
print("   np.sum()       → Add up all values")
print("   np.std()       → Standard deviation")
print("   np.argmax()    → Index of thet value")
print("   np.argmin()    → Index of the lowest value")
print("   np.sort()      → Sort the array")
print("   scores + 5     → Math on ALL values at once")
print("   scores >= 40   → Filter values by condition")
print("=" * 55)
print("\n✅ Project Complete! Try changing the marks above.")    

