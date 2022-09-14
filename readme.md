# Brik

This began as a way to read in lesson plan schedules from a popular online homeschool website and modify the dates, add or remove assignments and so on. A web UI was planned. The ability to read in schedules from diverse sources was planned. It has been shelved until further notice since it is not needed for now but may be again in the future.

## technical details

brik is a dynamic task scheduling and tracking system that allows mass import of tasks from pregenerated schedules. It allows for tasks to be weighted, and then uses those weights to distribute the tasks based on mappings for how much weight can happen on a day of the week. Or it can also distribute tasks to conclude by an end date.

Tasks are stored in mongodb and a flask api is planned to allow for a web ui and other integrations
