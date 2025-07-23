from neomodel import db
from app.models import Token, Project, File, User

def clear_db():
    print("Clearing Neo4j database...")
    db.cypher_query("MATCH (n) DETACH DELETE n")

def seed_data():
    print("Seeding Neo4j database...")

    token1 = Token(name="Access Token").save()
    token2 = Token(name="Refresh Token").save()

    project1 = Project(name="AI Analytics Platform").save()
    project2 = Project(name="E-Commerce Dashboard").save()

    file1 = File(filename="report_insights.png", width=200).save()
    file2 = File(filename="sales_graph.jpg", width=200).save()
    file3 = File(filename="user_behavior.csv", width=150).save()

    user = User(google_id="102718630068735143796").save()

    user.uploads.connect(file1)
    user.uploads.connect(file2)

    project1.files.connect(file1)
    project1.files.connect(file2)
    project2.files.connect(file3)

    print("Seed completed successfully!")

if __name__ == "__main__":
    clear_db()
    seed_data()
