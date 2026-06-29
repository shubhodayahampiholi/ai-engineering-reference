"""
Verify connectivity to the Databricks workspace.
"""

from ai_engineering_reference.workspace import get_workspace_client


def main() -> None:
    workspace = get_workspace_client()

    current_user = workspace.current_user.me()

    print("=" * 80)
    print("Successfully connected to Databricks")
    print("=" * 80)
    print(f"User : {current_user.user_name}")
    print(f"Name : {current_user.display_name}")


if __name__ == "__main__":
    main()