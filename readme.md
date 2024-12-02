# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

## **Closed Issue 1**: [Issue #1: Server returns 500 error despite successful user registration and overwrites the written Nickname](https://github.com/GxPatel/event_manager/blob/a590a8c8a2ca2f18f2751bd733e7ac5a523ec619/app/services/user_service.py#L54)
- Description:
When registering a new user, the server successfully stores the user data in the database, but the nickname overwrites the entered nickname and returns a 500 Internal Server Error response. This issue may occur because the nickname generation logic might be executed in an unintended order or conflict with the database operation. It points to a potential issue in the post-registration process or response serialization.

- Solution:
The issue is resolved by ensuring the nickname is properly assigned to the new user before the database commit and by sending the verification email only after the user has been successfully committed to the database. This prevents overwriting the nickname and avoids issues with the response.

## **Closed Issue 2**: [Issue #2: Validation Issues for Nickname and Bio in UserBase Schema](https://github.com/GxPatel/event_manager/blob/a590a8c8a2ca2f18f2751bd733e7ac5a523ec619/app/schemas/user_schemas.py#L25)
- Description:
•	Nicknames longer than 30 characters are not correctly rejected despite the max_length=30 constraint in the UserBase schema.
•	Bios longer than 500 characters are not restricted, leading to potential data inconsistencies.

- Solution:
•	Ensure that the UserBase schema validates the nickname and bio lengths correctly by applying proper constraints.
•	Add validation for bio and nickname in the Pydantic model, making sure that they respect the max_lengthconstraint.
 
## **Closed Issue 3**: [Issue #3: Email Verification Sends Email Before Database Commit](https://github.com/GxPatel/event_manager/blob/a590a8c8a2ca2f18f2751bd733e7ac5a523ec619/app/services/user_service.py#L54)
- Description:
In the create method, the email verification is sent (await email_service.send_verification_email(new_user)) before committing the user to the database. If the email fails to send, it could result in a user being added to the database without email verification.

- Solution:
Ensure that the email verification is only sent after the user is successfully committed to the database. This guarantees that no user is saved without a valid email verification.

## **Closed Issue 4**: [Issue #4: Password Reset Does Not Notify Users](https://github.com/GxPatel/event_manager/blob/a590a8c8a2ca2f18f2751bd733e7ac5a523ec619/app/services/user_service.py#L170)
- Description:
The reset_password method changes the user's password without sending any notification, which may cause confusion or security concerns among users who are unaware that their password has been reset.

- Solution:
Send a notification email to the user after the password is successfully reset, informing them of the change. This enhances security and transparency for the user.

## **Closed Issue 5**: [Issue #5: No Exception Details in _execute_query](https://github.com/GxPatel/event_manager/blob/a590a8c8a2ca2f18f2751bd733e7ac5a523ec619/app/services/user_service.py#L24)
- Description:
The _execute_query method logs errors but doesn't re-raise or handle exceptions explicitly, which may obscure details for debugging.

- Solution:
Enhance the exception handling within the _execute_query method by logging more detailed exception information and re-raising the exceptions for proper error handling upstream.

## **Closed Issue 6**: [Issue #6: No Soft Delete Implementation](https://github.com/GxPatel/event_manager/blob/a590a8c8a2ca2f18f2751bd733e7ac5a523ec619/app/services/user_service.py#L119)
- Description:
The delete method performs a hard delete on the user, which might lead to accidental data loss. Soft delete (marking data as deleted without removing it) is a safer option, particularly for user records.

- Solution:
Implement soft delete functionality by adding a deleted_at timestamp or is_deleted flag. This way, the user record is not permanently removed from the database, making it possible to restore if needed.


## Reflection on the Assignment

This assignment was an excellent opportunity to enhance both my technical and analytical skills while addressing real-world software challenges. Resolving the issues required a deep dive into the existing codebase, identifying root causes, and implementing robust solutions to ensure the system's reliability and maintainability. For instance, solving **Issue #1** and **Issue #3** improved my understanding of the importance of proper workflow sequencing in database operations, such as committing user data before executing additional steps like email verification. This insight highlighted the critical balance between system integrity and user experience.

Through this process, I gained a stronger appreciation for validation, error handling, and security in software development. Working on **Issue #2** emphasized the role of schema constraints in maintaining data consistency, while addressing **Issue #4** underscored the necessity of transparent communication with users for enhancing trust and security. Similarly, tackling **Issue #5** improved my knowledge of logging and exception handling best practices, which are essential for debugging and maintaining scalable systems. Implementing a soft delete in **Issue #6** reinforced the importance of data retention strategies, especially in user-facing applications where accidental data loss can have significant repercussions.

Overall, the challenges presented in this assignment were instrumental in sharpening my problem-solving abilities and deepening my understanding of collaborative processes in software development. The experience also reinforced the value of well-documented code and proactive communication within a team to streamline issue resolution and ensure alignment with project goals. These lessons will undoubtedly inform my future contributions to complex projects.
