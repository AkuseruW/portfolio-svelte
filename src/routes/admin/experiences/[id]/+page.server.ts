import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'
import { error } from '@sveltejs/kit';


export const load: PageServerLoad = async ({ params }) => {
    const experience = await fetch(`${SERVEUR_URL}/api/experiences/${params.id}`).then(res => res.json())
    if (experience) {
        return {
            experience
        }
    }

    throw error(404, 'Category not found');
}


export const actions: Actions = {
    update_experience: async ({ request }) => {
        const formData = await request.formData();

        const experiences = {
            title: formData.get('title'),
            description: formData.get('description'),
            startTime: formData.get('startTime'),
            endTime: formData.get('endTime'),
            link: formData.get('link'),
        }

        await fetch(`${SERVEUR_URL}/api/experiences/${formData.get('id')}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(experiences),
        })


        return { success: true };
    }

}