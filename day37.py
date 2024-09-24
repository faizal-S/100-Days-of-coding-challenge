def enrollment_stats(universities):
    # Extracting enrollment numbers and tuition fees into separate lists
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions

def mean(values):
    # Calculating the mean of a list of values
    return sum(values) / len(values)

def median(values):
    # Calculating the median of a list of values
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:  # even length
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:  # odd length
        return sorted_values[mid]

# List of Nigerian universities with mock enrollment and tuition data
universities = [
    ['University of Lagos', 50000, 200000],
    ['Obafemi Awolowo University', 40000, 150000],
    ['University of Ibadan', 30000, 180000],
    ['Ahmadu Bello University', 60000, 250000],
    ['University of Nigeria, Nsukka', 45000, 220000],
    ['Lagos State University', 35000, 170000],
    ['Federal University of Technology, Minna', 25000, 130000]
]

# Get enrollment numbers and tuition fees
enrollments, tuitions = enrollment_stats(universities)

# Calculate total values
total_students = sum(enrollments)
total_tuition = sum(tuitions)

# Calculate mean and median
student_mean = mean(enrollments)
student_median = median(enrollments)
tuition_mean = mean(tuitions)
tuition_median = median(tuitions)

# Output results
print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: ₦ {total_tuition:,}")
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print(f"Tuition mean: ₦ {tuition_mean:,.2f}")
print(f"Tuition median: ₦ {tuition_median:,}")
print("******************************")
