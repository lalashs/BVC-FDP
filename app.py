import streamlit as st

st.title("🎓 Student Percentage & Grade Calculator")

# Input number of subjects
num_subjects = st.number_input(
    "Enter number of subjects",
    min_value=1,
    step=1
)

marks = []
total_marks = 0

# Input marks for each subject
if num_subjects > 0:
    st.subheader("Enter marks for each subject (out of 100)")
    for i in range(int(num_subjects)):
        mark = st.number_input(
            f"Marks for Subject {i + 1}",
            min_value=0,
            max_value=100,
            step=1
        )
        marks.append(mark)

# Calculate result
if st.button("Calculate Result"):
    total_marks = sum(marks)
    max_marks = num_subjects * 100
    percentage = (total_marks / max_marks) * 100

    # Grade logic
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

    # Display results
    st.success("✅ Result Calculated Successfully!")
    st.write(f"*Total Marks:* {total_marks} / {max_marks}")
    st.write(f"*Percentage:* {percentage:.2f}%")
    st.write(f"*Grade:* {grade}")