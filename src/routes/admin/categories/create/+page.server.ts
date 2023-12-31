import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'


export const load: PageServerLoad = () => {

}


export const actions: Actions = {
    create_project: async ({ request }) => {
        const formData = await request.formData();
        const name = formData.get('name');

        if (!name) {
            return {
                error: 'Name is required'
            }
        }

        const category = {
            name
        }

        const res = await fetch(`${SERVEUR_URL}/api/categories/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(category),
        })

        if (res.ok) {
            return { success: true };
        } else {
            return {
                error: 'Failed to create category'
            }
        }

    }

}