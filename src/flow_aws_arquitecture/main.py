#!/usr/bin/env python
from random import randint

from crewai.flow import Flow, listen, start
from pydantic import BaseModel

from flow_aws_arquitecture.crews.poem_crew.aws_crew import AWSCrew


class AWSState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class AWSFlow(Flow[AWSState]):

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = (
            AWSCrew()
            .crew()
            .kickoff(
                inputs={
                    "url": "https://docs.aws.amazon.com/architecture-diagrams/latest/luminai-refinery-advisor-on-aws/luminai-refinery-advisor-on-aws.html?did=wp_card&trk=wp_card"
                }
            )
        )

    #     print("Poem generated", result.raw)
    #     self.state.poem = result.raw

    # @listen(generate_poem)
    # def save_poem(self):
    #     print("Saving poem")
    #     with open("poem.txt", "w") as f:
    #         f.write(self.state.poem)


def kickoff():
    poem_flow = AWSFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = AWSFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
