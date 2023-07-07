document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('taskInput');
    const addButton = document.getElementById('addButton');
    const taskList = document.getElementById('taskList');
  
    // Load tasks from localStorage
    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
  
    // Render tasks from the array
    function renderTasks() {
      taskList.innerHTML = '';
      tasks.forEach(function(task, index) {
        const li = document.createElement('li');
        const checkbox = document.createElement('input');
        const label = document.createElement('label');
        const deleteButton = document.createElement('button');
  
        checkbox.type = 'checkbox';
        checkbox.checked = task.completed;
        checkbox.addEventListener('change', function() {
          toggleTaskCompleted(index);
        });
  
        label.textContent = task.name;
        label.className = task.completed ? 'completed' : '';
  
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', function() {
          deleteTask(index);
        });
  
        li.appendChild(checkbox);
        li.appendChild(label);
        li.appendChild(deleteButton);
        taskList.appendChild(li);
      });
    }
  
    // Add a new task
    function addTask() {
      const taskName = taskInput.value.trim();
      if (taskName) {
        tasks.push({ name: taskName, completed: false });
        localStorage.setItem('tasks', JSON.stringify(tasks));
        taskInput.value = '';
        renderTasks();
      }
    }
  
    // Toggle task completed status
    function toggleTaskCompleted(index) {
      tasks[index].completed = !tasks[index].completed;
      localStorage.setItem('tasks', JSON.stringify(tasks));
      renderTasks();
    }
  
    // Delete a task
    function deleteTask(index) {
      tasks.splice(index, 1);
      localStorage.setItem('tasks', JSON.stringify(tasks));
      renderTasks();
    }
  
    addButton.addEventListener('click', addTask);
  
    taskInput.addEventListener('keyup', function(event) {
      if (event.keyCode === 13) {
        addTask();
      }
    });
  
    renderTasks();
  });
  