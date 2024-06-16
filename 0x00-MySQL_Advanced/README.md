Introduction

Projects Overview
Student Management System

    Objective: Designed a comprehensive database schema for a student management system.
    Components: Created tables for students, projects, and corrections, ensuring data integrity with foreign key constraints.
    Implementations:
        Developed stored procedures to compute average scores for students based on project contributions.
        Implemented functions like SafeDiv to handle edge cases, ensuring robust calculations.
        Built views to analyze student data and identify those needing attention based on scores and meeting histories.

Optimization Strategies

    Indexing: Utilized indexing strategies such as indexing the first letter of names and combining indexes with columns like scores to enhance query performance.
    Query Optimization: Optimized query execution plans and made adjustments to improve efficiency, especially in large datasets.

Technical Challenges

    Weighted Average Calculation: Implemented a stored procedure to compute the weighted average score considering different project weights. Used SQL functions to multiply scores by weights and divided the sum by the total weight, ensuring accuracy and reliability across various scenarios.
