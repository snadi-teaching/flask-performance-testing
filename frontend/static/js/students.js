
// Add student
document.getElementById('create-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        const response = await axios.post(`${API_URL}/students/`, {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            seniority: document.getElementById('seniority').value
        });
        alert('Student added successfully!');
        e.target.reset();
    } catch (error) {
        alert('Error adding student: ' + error.response?.data?.message || error.message);
    }
});
