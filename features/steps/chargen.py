from behave import *


@given('that we are in {location}')
def step_impl(context, location):
    """
    With this step we teleport test character to desired area. As I don't have
    imm powers we will rely on travel instead.

    :type location: str
    :type context: behave.runner.Context
    """
    prompt_location = 'Room name: %s' % location
    if context.search_buffer(context.buffers['login'], prompt_location):
        return True
    else:
        while not context.search_buffer(context.connection.buffer,
                                        prompt_location):
            context.connection.command_and_store('travel %s' % location)
            print(context.connection.buffer)
        return True


@when('we request "{item}"')
def step_impl(context, item):
    """
    :type context: behave.runner.Context
    :type item: str
    """
    command = 'say %s' % item
    context.connection.command_and_store(command)


@then('in inventory we should have "{string}"')
def step_impl(context, string):
    """
    :type context: behave.runner.Context
    :type string: str
    """
    context.connection.get_and_clear_buffer()
    context.connection.command_and_store('inventory')
    inventory_list = context.connection.get_and_clear_buffer()
    if not context.search_buffer(inventory_list, string):
        print(inventory_list)
        assert False


@step("we have empty inventory")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.connection.command_and_store('junk all')
