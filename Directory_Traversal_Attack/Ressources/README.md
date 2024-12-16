# Directory Traversal Attack

## Description
A directory traversal attack exploits insufficient input validation in a web application. By injecting special character sequences like `../` (dot-dot-slash), the attacker can navigate up the directory hierarchy on the server’s file system.

This allows access to files and directories outside the intended scope of the application, such as configuration files, source code, or sensitive system files like `/etc/passwd` on Linux systems.

## BornToSec
First, I noticed that the website was vulnerable to directory traversal. I navigated to the following URL:
```http
http://10.11.249.222/index.php?page=../../
```

And I got a different error than the usual "Wtf ?".
So continue to add a lot of `../` until I understood that the fact that i could navigate through the directories could expose some very sensitive files as the famous one `/etc/passwd`.

Then I navigated to the following URL:
```http
http://10.11.249.222/index.php?page=../../../../../../../etc/passwd
```

And I got the flag.

## How to prevent it
- Validate and Sanitize Input: Ensure that user-supplied input is strictly validated. Reject inputs containing `../`, `/`, or similar patterns.
- Use Allow Lists: Restrict file access to a predefined list of safe and expected files.
- Canonicalize Paths: Use functions like `realpath()` (in PHP) or equivalent in other languages to resolve and verify file paths against an allowed base directory.
- Restrict File Permissions: Limit access to sensitive files and directories using proper file system permissions.
- Use Built-in Security Features: Many frameworks provide secure methods for handling file paths that automatically prevent traversal attacks.